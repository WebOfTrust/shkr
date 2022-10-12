SHELL := /bin/zsh
DIR = $(shell pwd)

clean:
	rm -rf build dist

build: clean
	pyinstaller --clean --noconfirm main.spec

package:
	pushd dist; \
	productbuild --identifier $(SHKR_IDENT) --sign $(SHKR_INSTALLER) --component shkr.app /Applications shkr.pkg

notarize:
	pushd dist; \
	xcrun notarytool submit shkr.pkg --keychain-profile $(SHKR_IDENT) --wait

staple:
	pushd dist; \
	xcrun stapler staple shkr.pkg

publish: build package notarize staple
