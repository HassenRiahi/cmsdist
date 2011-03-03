### RPM external yui 2.8.2r1
Source: http://yuilibrary.com/downloads/yui2/yui_%realversion.zip 

%prep
rm -rf %{_builddir}/yui
mkdir -p %{_builddir}/yui
cd %{_builddir}
unzip %{_sourcedir}/yui_%realversion.zip 
%build
%install
pwd
cp -r yui/* %i
mkdir -p %i/etc
cat << \EOF_CHERRYPY_CONF > %i/etc/cherrypy.conf
# Serve a complete directory 
[/] 
tools.staticdir.on = True 
tools.staticdir.dir = %i/build
EOF_CHERRYPY_CONF
%post
%{relocateConfig}etc/cherrypy.conf
