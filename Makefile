

link=https://github.com/ntegan1/opsetspeed/raw/zprebuild-v2/buildtgz.zip

all:
	$(RM) -r build
	$(RM) buildtgz.zip
	wget $(link)
	./unzip
	$(RM) buildtgz.zip
	$(RM) build.tgz
