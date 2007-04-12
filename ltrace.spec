%define name	ltrace
%define version	0.5

%define svn		45svn
%define release	%mkrel 1.%svn

Summary:	Track runtime library calls from dynamically linked executables
Name:		%{name}
Version:	%{version}
Release:	%{release}
Url:		ftp://ftp.debian.org/debian/pool/main/l/ltrace/
# Taken from fedora:
Source0:	ltrace-%{version}.tar.bz2
# fedora patches:
Patch2: ltrace-opd.patch
Patch3: ltrace-ppc32fc5.patch
Patch4: ltrace-0.5-gnuhash.patch
Patch5: ltrace-0.5-testsuite.patch
# debian patch:
Patch100:		ftp://ftp.debian.org/debian/pool/main/l/ltrace/ltrace_0.4-1.diff.gz
License:	GPL
Group:		Development/Other
ExclusiveArch:	%{ix86} x86_64 ppc x86_64 sparc alpha
BuildRequires:	elfutils-devel
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
%setup -q

%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1

%patch100 -p1

%build
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
%doc debian/changelog COPYING README TODO BUGS
%{_bindir}/ltrace
%{_mandir}/man1/ltrace.1*
%config(noreplace) %{_sysconfdir}/ltrace.conf

