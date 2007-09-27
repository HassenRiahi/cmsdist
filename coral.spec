### RPM cms coral CORAL_1_9_0-CMS1
## IMPORT configurations
Provides: /bin/zsh
Requires: coral-tool-conf
Patch:    coral-SV1BuildFiles
Patch1:   coral_1_8_1_typefixes

%define cvsprojuc       %(echo %n | sed -e "s|-debug||"| tr 'a-z' 'A-Z')
%define cvsprojlc       %(echo %cvsprojuc | tr 'A-Z' 'a-z')
%define cvsdir          %cvsprojlc
%define cvsserver       %cvsprojlc
%define preBuildCommand (rm -rf LFCLookupService LFCReplicaService MySQLAccess)
%define prebuildtarget  prebuild
%define buildtarget     release-build
%define patchsrc        %patch -p0
%define patchsrc2       %patch1 -p0

## IMPORT lcg-scram-build
## IMPORT cms-scram-build
## IMPORT scramv1-build
