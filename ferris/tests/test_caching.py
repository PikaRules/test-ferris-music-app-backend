from ferrisnose import AppEngineTest
from google.appengine.api import memcache
from ferris.core.caching import cache, none_sentinel_string, LocalBackend, MemcacheBackend, DatastoreBackend, MemcacheCompareAndSetBackend, LayeredBackend


class CacheTest(AppEngineTest):

    def test_cache(self):
        for backend in [LocalBackend, MemcacheBackend, DatastoreBackend, MemcacheCompareAndSetBackend, LayeredBackend(LocalBackend, MemcacheBackend)]:
            memcache.flush_all()
            LocalBackend.reset()

            mutators = [0, 0, 0]
            print 'testing %s' % backend

            @cache('cache-test-key', backend=backend)
            def test_cached():
                mutators[0] += 1
                return mutators[0]

            assert test_cached() == 1
            assert test_cached() == 1
            assert mutators[0] == 1
            assert backend.get('cache-test-key') == 1
            assert test_cached.uncached() == 2
            assert test_cached.cached() == 1

            test_cached.clear_cache()
            assert test_cached() == 3

            @cache('cache-test-key-none', backend=backend)
            def test_cached_with_none():
                mutators[1] += 1
                return None

            assert test_cached_with_none() is None
            assert test_cached_with_none() is None
            assert mutators[1] == 1
            assert backend.get('cache-test-key-none') == none_sentinel_string
