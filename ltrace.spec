%define snapshot 1
%define git d66c8b1

Summary:	Track runtime library calls from dynamically linked executables
Name:		ltrace
Version:	0.7.2
Release:	1
License:	GPLv2+
Group:		Development/Other
URL:		http://ltrace.alioth.debian.org/
# snapshot from http://anonscm.debian.org/gitweb/?p=collab-maint/ltrace.git
Source0:	ltrace-%{git}.tar.gz
# fedora patch:
Patch5:		ltrace-0.5-testsuite.patch
ExclusiveArch:	%{ix86} x86_64 ppc x86_64 sparc alpha
BuildRequires:	elfutils-devel
%if %snapshot
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

%if %snapshot
%setup -q -n %{name}-%{git}
%else
%setup -q
%endif

#%patch5 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing -fPIC"
export CXXFLAGS="%{optflags} -fno-strict-aliasing -fPIC"

%if %snapshot
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
%doc README TODO
%config(noreplace) %{_sysconfdir}/ltrace.conf
%{_bindir}/ltrace
%{_mandir}/man1/ltrace.1*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6-0.81.6mdv2011.0
+ Revision: 666102
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-0.81.5mdv2011.0
+ Revision: 606425
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-0.81.4mdv2010.1
+ Revision: 520148
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.6-0.81.3mdv2010.0
+ Revision: 426014
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.6-0.81.2mdv2009.1
+ Revision: 351543
- rebuild

* Fri Aug 01 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6-0.81.1mdv2009.0
+ Revision: 259366
- new svn snap (r81)
- drop P100, it's in there
- fix build

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.6-0.77.1mdv2009.0
+ Revision: 219562
- rebuild
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 22 2007 Adam Williamson <awilliamson@mandriva.org> 0.6-0.77.1mdv2008.0
+ Revision: 68826
- rebuild for 2008
- don't package debian changelog and license
- strip debian patch of debian-specific stuff
- drop patches 2, 3 and 4 (merged or equivalent merged upstream)
- update URLs
- use Fedora license policy
- update to latest SVN rev 77
- correct versioning
- spec clean


* Fri Aug 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.5-1.45svnmdv2007.0
- new release
- added fedorad patches
- updated debian (useless for now)

* Fri Aug 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.4-1mdv2007.0
- new release (#24430)
- kill patch 2: merged upstream

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.3.36-3mdk
- Rebuild

* Thu Jan 13 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.36-2mdk
- fix buildrequires

* Thu Jan 13 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.3.36-1mdk
- 0.3.36 (sync with fedora)
- build on alpha & sparc too

