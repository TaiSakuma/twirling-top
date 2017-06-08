
##__________________________________________________________________||
import alphatwirl

##__________________________________________________________________||
class TwilightTree(object):
    def __init__(self, tree):
        self.tree = tree

    def __repr__(self):
        name_value_pairs = (
            ('tree', self.tree),
        )
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(['{} = {!r}'.format(n, v) for n, v in name_value_pairs]),
        )

    def summarize(self, tblcfg, max_events = -1):

        default_cfg = dict(
            outFile = False,
        )
        tblcfg = self._complement_tblcfg_with_default(tblcfg, default_cfg)

        tableConfigCompleter = alphatwirl.configure.TableConfigCompleter(
            defaultSummaryClass = alphatwirl.summary.Count,
            createOutFileName = alphatwirl.configure.TableFileNameComposer2(default_prefix = 'tbl_n')
        )
        tblcfg = [tableConfigCompleter.complete(c) for c in tblcfg]
        reader_collector_pairs = [build_counter_collector_pair(c) for c in tblcfg]

        reader = alphatwirl.loop.ReaderComposite()
        collector = alphatwirl.loop.CollectorComposite()
        for r, c in reader_collector_pairs:
            reader.add(r)
            collector.add(c)
        eventBuilder =  EventBuilder(self.tree, max_events = max_events)
        eventLoop = alphatwirl.loop.EventLoop(eventBuilder, reader)
        reader = eventLoop()
        return collector.collect(((None, (reader, )), ))

    def scan(self, tblcfg, max_events = 10):

        default_cfg = dict(
            keyAttrNames = ( ),
            sort = False,
            summaryClass = alphatwirl.summary.Scan
        )
        tblcfg = self._complement_tblcfg_with_default(tblcfg, default_cfg)
        return self.summarize(tblcfg, max_events = max_events)

    def _complement_tblcfg_with_default(self, tblcfg, default_cfg):
        for cfg in tblcfg:
            default_cfg_copy =  default_cfg.copy()
            default_cfg_copy.update(cfg)
            cfg.clear()
            cfg.update(default_cfg_copy)
        return tblcfg


##__________________________________________________________________||
class EventBuilder(object):
    def __init__(self, tree, max_events = -1):
        self.tree = tree
        self.max_events = max_events

    def __repr__(self):
        name_value_pairs = (
            ('tree', self.tree),
        )
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(['{} = {!r}'.format(n, v) for n, v in name_value_pairs]),
        )

    def __call__(self):
        events = alphatwirl.roottree.BEvents(self.tree, maxEvents = self.max_events)
        return events

##__________________________________________________________________||
def build_counter_collector_pair(tblcfg):
    keyValComposer = alphatwirl.summary.KeyValueComposer(
        keyAttrNames = tblcfg['keyAttrNames'],
        binnings = tblcfg['binnings'],
        keyIndices = tblcfg['keyIndices'],
        valAttrNames = tblcfg['valAttrNames'],
        valIndices = tblcfg['valIndices']
    )
    nextKeyComposer = alphatwirl.summary.NextKeyComposer(tblcfg['binnings']) if tblcfg['binnings'] is not None else None
    summarizer = alphatwirl.summary.Summarizer(
        Summary = tblcfg['summaryClass']
    )
    reader = alphatwirl.summary.Reader(
        keyValComposer = keyValComposer,
        summarizer = summarizer,
        nextKeyComposer = nextKeyComposer,
        weightCalculator = tblcfg['weight'],
        nevents = tblcfg['nevents']
    )
    resultsCombinationMethod = alphatwirl.collector.ToDataFrame(
        summaryColumnNames = tblcfg['keyOutColumnNames'] + tblcfg['valOutColumnNames']
    )
    deliveryMethod = None
    collector = alphatwirl.loop.Collector(resultsCombinationMethod, deliveryMethod)
    return reader, collector

##__________________________________________________________________||
