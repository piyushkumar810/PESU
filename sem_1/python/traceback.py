# ----------------------- use traceback module
import sys
import traceback

old_limit=getattr(sys,"tracebacklimit", None)
sys.tracebacklimit=1
try:
    def a():
        def b():
            raise ValueError("demo error for traceback")
        b()
    a()
except Exception as e:
    print("exception caught .sys. tracebacklimit= ", sys.tracebacklimit)
    traceback.print_exc()
finally:
    # restore
    if old_limit is None:
        delattr(sys,"tracebacklimit")
    else:
        sys.tracebacklimit=old_limit