import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
