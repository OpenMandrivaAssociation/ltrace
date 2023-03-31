%define	Werror_cflags %nil


Summary:	Track runtime library calls from dynamically linked executables
Name:		ltrace
Version:	0.7.91
Release:	7
License:	GPLv2+
Group:		Development/Other
Url:		http://ltrace.alioth.debian.org/
# Note: this URL needs to be updated for each release, as the file
# number changes for each file.  Full list of released files is at:
#  https://alioth.debian.org/frs/?group_id=30892
Source0: ltrace-%{version}.tar.bz2

# Merge of several upstream commits that fixes compilation on ARM.
Patch0: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-arm.patch
 
# Upstream patch that fixes accounting of exec, __libc_start_main and
# others in -c output.
Patch1: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-account_execl.patch
 
# Upstream patch that fixes interpretation of PLT on x86_64 when
# IRELATIVE slots are present.
Patch2: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-x86_64-irelative.patch
 
# Upstream patch that fixes fetching of system call arguments on s390.
Patch3: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-s390-fetch-syscall.patch
 
# Upstream patch that enables tracing of IRELATIVE PLT slots on s390.
Patch4: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-s390-irelative.patch
 
# Fix for a regression in tracing across fork.  Upstream patch.
Patch5: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-ppc64-fork.patch
 
# Fix crashing a prelinked PPC64 binary which makes PLT calls through
# slots that ltrace doesn't trace.
# https://bugzilla.redhat.com/show_bug.cgi?id=1051221
Patch6: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-breakpoint-on_install.patch
Patch7: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-ppc64-unprelink.patch
 
# Man page nits.  Backport of an upstream patch.
Patch8: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-man.patch
 
# https://bugzilla.redhat.com/show_bug.cgi?id=1044766
Patch9: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-cant_open.patch
 
# Support Aarch64 architecture.
Patch10: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-aarch64.patch
 
# https://bugzilla.redhat.com/show_bug.cgi?id=1064406
Patch11: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.2-e_machine.patch
 
# Support for ppc64le, backported from upstream.
# http://anonscm.debian.org/gitweb/?p=collab-maint/ltrace.git;a=commit;h=eea4ad2cce289753aaa35b4e0258a76d8f8f367c
# https://bugzilla.redhat.com/show_bug.cgi?id=1131956
Patch13: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-ppc64le-support.patch
# 35a9677dc9dcb7909ebd28f30200474d7e8b660f,
# 437d2377119036346f4dbd93039c847b4cc9d0be,
# eb3993420734f091cde9a6053ca6b4edcf9ae334
Patch14: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-ppc64le-fixes.patch
 
# http://anonscm.debian.org/gitweb/?p=collab-maint/ltrace.git;a=commit;h=2e9f9f1f5d0fb223b109429b9c904504b7f638e2
# http://anonscm.debian.org/gitweb/?p=collab-maint/ltrace.git;a=commit;h=f96635a03b3868057db5c2d7972d5533e2068345
Patch15: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-parser-ws_after_id.patch
 
# https://bugzilla.redhat.com/show_bug.cgi?id=1171165
# http://anonscm.debian.org/cgit/collab-maint/ltrace.git/commit/?id=d8f1287b85e2c2b2ae0235809e956f4365e53c45
# http://anonscm.debian.org/cgit/collab-maint/ltrace.git/commit/?id=d80c5371454383e3f9978622e5578cf02af8c44c
# http://anonscm.debian.org/cgit/collab-maint/ltrace.git/commit/?id=bf82100966deda9c7d26ad085d97c08126a8ae88
Patch16: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-ppc-bias.patch
 
# https://bugzilla.redhat.com/show_bug.cgi?id=1158714
Patch17: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-x86-plt_map.patch
Patch18: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-x86-unused_label.patch
 
# https://bugzilla.redhat.com/show_bug.cgi?id=1170315
Patch19: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-unwind-elfutils.patch
 
# https://bugzilla.redhat.com/show_bug.cgi?id=1208351
# http://anonscm.debian.org/cgit/collab-maint/ltrace.git/commit/?id=4724bd5a4a19db117a1d280b9d1a3508fd4e03fa
# http://anonscm.debian.org/cgit/collab-maint/ltrace.git/commit/?id=72ee29639c55b5942bc07c8ed0013005f8fc5a97
Patch20: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-multithread-no-f-1.patch
Patch21: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-multithread-no-f-2.patch
 
# Fix problems with building a number of test cases.
# http://anonscm.debian.org/cgit/collab-maint/ltrace.git/commit/?id=694d19ff14017926454771cbb63a22355b72f1bf
# http://anonscm.debian.org/cgit/collab-maint/ltrace.git/commit/?id=a3a03622fb4ca9772dca13eae724a94ba1e728f4
Patch22: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-testsuite-includes.patch
Patch23: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-testsuite-includes-2.patch
 
# https://bugzilla.redhat.com/show_bug.cgi?id=1210653
# http://anonscm.debian.org/cgit/collab-maint/ltrace.git/commit/?id=eea6091f8672b01f7f022b0fc367e0f568225ffc
Patch24: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-ppc64le-configure.patch
 
Patch25: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-rh1307754.patch
 
# GCC now warns (errors) on "tautological compares", and readdir_r is deprecated.
Patch26: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-tautology.patch
 
# ARM code has unreachable code after switch statement, move initialization
Patch27: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-rh1423913.patch
 
# AARCH64 large parameters and syscall testsuite fixes.
Patch28: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-aarch64-params.patch
 
# gcc-9 fix.  Avoid passing NULL as argument to %s
Patch29: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-null.patch
 
# Adds support for CET PLTs via second-plt lookups.
Patch30: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-cet.patch
 
# Extra #includes for gcc 9
Patch31: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-aarch64-headers.patch
# Testsuite: AARCH64 ifuncs not supported yet yet.
Patch32: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-rh1225568.patch
 
# testsuite fixes for pre-installed config files
Patch33: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-testsuite-system_call_params.patch
 
# Ignore bogus files from the environment
Patch34: https://src.fedoraproject.org/rpms/ltrace/raw/master/f/ltrace-0.7.91-XDG_CONFIG_DIRS.patch

Patch100: ltrace-0.7.91-aarch64-extra-structs.patch

BuildRequires:	elfutils-devel

%description
Ltrace is a debugging program which runs a specified command until the command
exits. While the command is executing, ltrace intercepts and records both the
dynamic library calls called by the executed process and the signals received
by the executed process. Ltrace can also intercept and print system calls
executed by the process.

You should install ltrace if you need a sysadmin tool for tracking the
execution of processes.

%prep
%setup -q
%autopatch -p1
autoconf
libtoolize --copy --force
autoreconf -fiv

%build
export CFLAGS="%{optflags} -fno-strict-aliasing -fPIC"
export CXXFLAGS="%{optflags} -fno-strict-aliasing -fPIC"

%configure --disable-werror
%make

%install
%makeinstall_std

# remove unpackaged files
rm -rf %{buildroot}%{_prefix}/doc
rm -fr %{buildroot}%_docdir/%name

%files
%doc README TODO
%{_bindir}/ltrace
%{_mandir}/man1/ltrace.1*
%{_mandir}/man5/ltrace.conf.5*
%{_datadir}/%{name}/libacl.so.conf
%{_datadir}/%{name}/libc.so.conf
%{_datadir}/%{name}/libm.so.conf
%{_datadir}/%{name}/syscalls.conf
