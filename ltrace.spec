%define	Werror_cflags %nil


Summary:	Track runtime library calls from dynamically linked executables
Name:		ltrace
Version:	0.7.91
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://ltrace.alioth.debian.org/
# Note: this URL needs to be updated for each release, as the file
# number changes for each file.  Full list of released files is at:
#  https://alioth.debian.org/frs/?group_id=30892
Source0: ltrace-%{version}.tar.bz2

# Merge of several upstream commits that fixes compilation on ARM.
Patch0: ltrace-0.7.91-arm.patch

# Upstream patch that fixes accounting of exec, __libc_start_main and
# others in -c output.
Patch1: ltrace-0.7.91-account_execl.patch

# Upstream patch that fixes interpretation of PLT on x86_64 when
# IRELATIVE slots are present.
Patch2: ltrace-0.7.91-x86_64-irelative.patch

# Upstream patch that fixes fetching of system call arguments on s390.
Patch3: ltrace-0.7.91-s390-fetch-syscall.patch

# Upstream patch that enables tracing of IRELATIVE PLT slots on s390.
Patch4: ltrace-0.7.91-s390-irelative.patch

# Fix for a regression in tracing across fork.  Upstream patch.
Patch5: ltrace-0.7.91-ppc64-fork.patch

# Fix crashing a prelinked PPC64 binary which makes PLT calls through
# slots that ltrace doesn't trace.
# https://bugzilla.redhat.com/show_bug.cgi?id=1051221
Patch6: ltrace-0.7.91-breakpoint-on_install.patch
Patch7: ltrace-0.7.91-ppc64-unprelink.patch

# Man page nits.  Backport of an upstream patch.
Patch8: ltrace-0.7.91-man.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1044766
Patch9: ltrace-0.7.91-cant_open.patch

# Support Aarch64 architecture.
Patch10: ltrace-0.7.91-aarch64.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1064406
Patch11: ltrace-0.7.2-e_machine.patch


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
%apply_patches
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
%config(noreplace) %{_sysconfdir}/ltrace.conf
%{_bindir}/ltrace
%{_mandir}/man1/ltrace.1*
%{_mandir}/man5/ltrace.conf.5*
