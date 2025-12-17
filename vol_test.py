from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

#! get default audio device
devices = AudioUtilities.GetSpeakers()
print(type(devices))

# Use the _dev attribute to access the underlying IMMDevice
interface = devices._dev.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = cast(interface, POINTER(IAudioEndpointVolume))

#! get current vol level
current = volume.GetMasterVolumeLevelScalar()
print(f"Current volume: {int(current * 100)}%")

#! set vol to 50%
volume.SetMasterVolumeLevelScalar(0.5, None)
print("Volume set to 50%")