import os
import shutil
import platform
import rumps


def main():
    sodium = 'libsodium.23.arm.dylib' if platform.processor() == 'arm' else 'libsodium.23.i386.dylib'
    print(sodium)
    lib_home = os.path.expanduser("~/lib")
    if not os.path.exists(lib_home):
        os.makedirs(lib_home)

    b = shutil.copy(f'/Applications/shkr.app/Contents/MacOS/{sodium}', os.path.join(lib_home, 'libsodium'))
    rumps.notification("Shkr", "libsodium installed at ", f"{b}")


if __name__ == '__main__':
    main()
