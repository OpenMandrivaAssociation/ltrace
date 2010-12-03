%define svn 81
%if %svn
%define release %mkrel 0.%svn.5
%else
%define release %mkrel 3
%endif

Summary:	Track runtime library calls from dynamically linked executables
Name:		ltrace
Version:	0.6
Release:	%{release}
License:	GPLv2+
Group:		Development/Other
URL:		http://svn.debian.org/wsvn/ltrace
# check out svn://svn.debian.org/ltrace/ltrace/trunk and compress
Source0:	ltrace-%{svn}.tar.bz2
# fedora patch:
Patch5:		ltrace-0.5-testsuite.patch
ExclusiveArch:	%{ix86} x86_64 ppc x86_64 sparc alpha
BuildRequires:	elfutils-devel
%if %svn
BuildRequires:	autoconf
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Ltrace is a debugging program which runs a specified command until the command
exits. While the command is executing, ltrace intercepts and records both the
dynamic library calls called by the executed process and the signals received
by the executed process. Ltrace can also intercept and print system calls
executed by the process.

You should install ltrace if you need a sysadmin tool for tracking the
execution of processes.

%prep

%if %svn
%setup -q -n %{name}
%else
%setup -q
%endif

%patch5 -p1

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE=1"
%if %svn
./autogen.sh
%endif
%configure
%make

%install
rm -rf %{buildroot}

%makeinstall_std

# remove unpackaged files
rm -rf %{buildroot}%{_prefix}/doc
rm -fr %{buildroot}%_docdir/%name

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO BUGS
%config(noreplace) %{_sysconfdir}/ltrace.conf
%{_bindir}/ltrace
%{_mandir}/man1/ltrace.1*
