# http://www.microsoft.com/technet/scriptcenter/funzone/games/sapi.mspx
# ../gen/_C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_0
# http://thread.gmane.org/gmane.comp.python.ctypes.user/1485

import os, unittest, tempfile
from comtypes.client import CreateObject

class Test(unittest.TestCase):
    def test(self):
        engine = CreateObject("SAPI.SpVoice")
        stream = CreateObject("SAPI.SpFileStream")
        from comtypes.gen import SpeechLib

        fd, fname = tempfile.mkstemp(suffix=".wav")
        os.close(fd)
        
        stream.Open(fname, SpeechLib.SSFMCreateForWrite)

        # engine.AudioStream is a propputref property
        engine.AudioOutputStream = stream
        self.failUnlessEqual(engine.AudioOutputStream, stream)
        engine.speak("Hello, World", 0)
        stream.Close()
        filesize = os.stat(fname).st_size
        self.failUnless(filesize > 100, "filesize only %d bytes" % filesize)
        os.unlink(fname)
        
    def test_dyndisp(self):
        from comtypes.client.dynamic import _Dispatch
        engine = _Dispatch(CreateObject("SAPI.SpVoice"))
        stream = _Dispatch(CreateObject("SAPI.SpFileStream"))

        from comtypes.gen import SpeechLib

        fd, fname = tempfile.mkstemp(suffix=".wav")
        os.close(fd)
        
        stream.Open(fname, SpeechLib.SSFMCreateForWrite)

        # engine.AudioStream is a propputref property
        engine.AudioOutputStream = stream
        self.failUnlessEqual(engine.AudioOutputStream, stream._comobj)
        engine.speak("Hello, World", 0)
        stream.Close()
        filesize = os.stat(fname).st_size
        self.failUnless(filesize > 100, "filesize only %d bytes" % filesize)
        os.unlink(fname)

if __name__ == "__main__":
    unittest.main()
