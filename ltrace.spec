%define snapshot 1
%define git d66c8b1

Summary:	Track runtime library calls from dynamically linked executables
Name:		ltrace
Version:	0.7.2
Release:	6
License:	GPLv2+
Group:		Development/Other
Url:		http://ltrace.alioth.debian.org/
# snapshot from http://anonscm.debian.org/gitweb/?p=collab-maint/ltrace.git
Source0:	ltrace-%{git}.tar.gz
Patch0:		ltrace-0.7.2-gcc48.patch
ExclusiveArch:	%{ix86} x86_64 ppc x86_64 sparc alpha %{arm}
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
%if %snapshot
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%apply_patches

%build
export CFLAGS="%{optflags} -fno-strict-aliasing -fPIC"
export CXXFLAGS="%{optflags} -fno-strict-aliasing -fPIC"

%if %snapshot
./autogen.sh
%endif
%configure2_5x
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

