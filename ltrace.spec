%define name	ltrace
%define version	0.6
%define svn	77
%if %svn
%define release	%mkrel 0.%svn.1
%else
%define release	%mkrel 4
%endif

Summary:	Track runtime library calls from dynamically linked executables
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://svn.debian.org/wsvn/ltrace
# check out svn://svn.debian.org/ltrace/ltrace/trunk and compress
Source0:	ltrace-%{svn}.tar.bz2
# fedora patch:
Patch5:		ltrace-0.5-testsuite.patch
# debian patch, stripped of debian-specific stuff:
Patch100:	ltrace_0.4-2.diff
License:	GPLv2+
Group:		Development/Other
ExclusiveArch:	%{ix86} x86_64 ppc x86_64 sparc alpha
BuildRequires:	elfutils-devel
%if %svn
BuildRequires:	autoconf
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Ltrace is a debugging program which runs a specified command until the
command exits.  While the command is executing, ltrace intercepts and
records both the dynamic library calls called by the executed process
and the signals received by the executed process.  Ltrace can also
intercept and print system calls executed by the process.

You should install ltrace if you need a sysadmin tool for tracking the
execution of processes.

%prep
%if %svn
%setup -q -n %{name}
%else
%setup -q
%endif

%patch5 -p1

%patch100 -p1

%build
%if %svn
./autogen.sh
%endif
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}
# remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc
rm -fr $RPM_BUILD_ROOT%_docdir/%name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO BUGS
%{_bindir}/ltrace
%{_mandir}/man1/ltrace.1*
%config(noreplace) %{_sysconfdir}/ltrace.conf

