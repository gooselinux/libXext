Summary: X.Org X11 libXext runtime library
Name: libXext
Version: 1.1
Release: 3%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
# From upstream, drop if updating to 1.1.1
Patch1: libXext-1.1-XAllocID.patch

BuildRequires: xorg-x11-proto-devel >= 7.4-23
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool pkgconfig

%description
X.Org X11 libXext runtime library

%package devel
Summary: X.Org X11 libXext development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

Requires: libX11-devel pkgconfig
# xorg-x11-proto-devel is needed by xext.pc
Requires: xorg-x11-proto-devel >= 7.0-1


%description devel
X.Org X11 libXext development package

%prep
%setup -q
%patch1 -p1 

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_libdir}/libXext.so.6
%{_libdir}/libXext.so.6.4.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/MITMisc.h
%{_includedir}/X11/extensions/XEVI.h
%{_includedir}/X11/extensions/XLbx.h
%{_includedir}/X11/extensions/XShm.h
%{_includedir}/X11/extensions/Xag.h
%{_includedir}/X11/extensions/Xcup.h
%{_includedir}/X11/extensions/Xdbe.h
%{_includedir}/X11/extensions/Xext.h
%{_includedir}/X11/extensions/Xge.h
%{_includedir}/X11/extensions/dpms.h
%{_includedir}/X11/extensions/extutil.h
%{_includedir}/X11/extensions/lbxbuf.h
%{_includedir}/X11/extensions/lbxbufstr.h
%{_includedir}/X11/extensions/lbximage.h
%{_includedir}/X11/extensions/multibuf.h
%{_includedir}/X11/extensions/security.h
%{_includedir}/X11/extensions/shape.h
%{_includedir}/X11/extensions/sync.h
%{_includedir}/X11/extensions/xtestext1.h
%{_libdir}/libXext.so
%{_libdir}/pkgconfig/xext.pc
#%dir %{_mandir}/man3x
%{_mandir}/man3/*.3*

%changelog
* Mon Jul 19 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.1-3
- libXext-1.1-event_vec-smash.patch: drop, this patch is wrong and has been
  reverted upstream. (#614888)

* Thu Dec 03 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.1-2
- libXext-1.1-XAllocID.patch: call XAllocID with the display lock held.
- libXext-1.1-event_vec-smash.patch: don't smash the event processing vector
  if the server has an older extension version than the client.

* Tue Oct 06 2009 Adam Jackson <ajax@redhat.com> 1.1-1
- libXext 1.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.99.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.0.99.4-2
- Un-require xorg-x11-filesystem

* Wed Jul 22 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.0.99.4-1
- libXext 1.0.99.4
- fix.patch: Drop.

* Tue Jul 21 2009 Adam Jackson <ajax@redhat.com> 1.0.99.2-0
- libXext snapshot

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 19 2008 Adam Jackson <ajax@redhat.com> 1.0.99.1-1
- libXext 1.0.99.1

* Wed Dec 17 2008 Matthias Clasen <mclasen@redhat.com> 1.0.4-2
- Rebuild for pkg-config auto-provides

* Fri Feb 29 2008 Adam Jackson <ajax@redhat.com> 1.0.4-1
- libXext 1.0.4

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.1-6
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 parag <paragn@fedoraproject.org> - 1.0.1-5
- Merge-Review #226070
- Removed XFree86-libs, xorg-x11-libs XFree86-devel, xorg-x11-devel as Obsoletes
- Removed BR:pkgconfig
- Removed zero-length README file

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.0.1-4
- Rebuild for build id

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> 1.0.1-4
- Don't install INSTALL

* Tue Oct 3 2006 Adam Jackson <ajackson@redhat.com> 1.0.1-3
- Force xorg-x11-proto-devel on >= 7.1-10 (for LBX headers), and rebuild.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-2.1
- rebuild

* Wed Jun 07 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-2
- Replace "makeinstall" with "make install DESTDIR=..."
- Remove package ownership of mandir/libdir/etc.

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 1.0.1-1
- Update to 1.0.1

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Mike A. Harris <mharris@redhat.com> 1.0.0-3
- Added "Requires: xorg-x11-proto-devel >= 7.0-1" to devel package (#173713)
- Added "libX11-devel" to devel package (#176078)

* Mon Jan 23 2006 Mike A. Harris <mharris@redhat.com> 1.0.0-2
- Bumped and rebuilt

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated libXext to version 1.0.0 from X11R7 RC4

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 0.99.3-1
- Updated libXext to version 0.99.3 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Updated libXext to version 0.99.2 from X11R7 RC2
- Changed 'Conflicts: XFree86-devel, xorg-x11-devel' to 'Obsoletes'
- Changed 'Conflicts: XFree86-libs, xorg-x11-libs' to 'Obsoletes'

* Fri Oct 21 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated to libXext-0.99.1 from the X11R7 RC1 release.
- Added manpages that were absent in X11R7 RC0, and updated the file lists
  to find them in section "man3x".

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-3
- Renamed package to remove xorg-x11 from the name due to unanimous decision
  between developers.
- Use Fedora Extras style BuildRoot tag.
- Disable static library creation by default.
- Add missing defattr to devel subpackage
- Add missing documentation files to doc macro

* Tue Aug 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-2
- Renamed package to prepend "xorg-x11" to the name for consistency with
  the rest of the X11R7 packages.
- Added "Requires: %%{name} = %%{version}-%%{release}" dependency to devel
  subpackage to ensure the devel package matches the installed shared libs.
- Added virtual "Provides: lib<name>" and "Provides: lib<name>-devel" to
  allow applications to use implementation agnostic dependencies.
- Added post/postun scripts which call ldconfig.
- Added Conflicts with XFree86-libs and xorg-x11-libs to runtime package,
  and Conflicts with XFree86-devel and xorg-x11-devel to devel package.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-1
- Initial build.
