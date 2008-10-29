Name:          mplayerthumbs
Summary:       Video thumbnail generator for KDE4 file managers
Version:       1.1
Release:       %mkrel 1
Source:        41180-%name-%version.tar.bz2
URL:           http://kde-apps.org/content/show.php/MPlayerThumbs?content=41180
License:       GPL
Group:         Graphical desktop/KDE
BuildRoot:     %{_tmppath}/%{name}-buildroot
Requires:      mplayer

%description
MPlayerThumbs is a video thumbnail generator for KDE file managers 
(Konqueror, Dolphin, ...) , now available also for KDE 4.
It needs mplayer (of course) to generate thumbnails, and it contains 
no linking to any library, so in a x86_64 system you can freely use the 
32bit mplayer binary with win32codecs by configuring the application launching 
the mplayerthumbsconfig helper application.
It catches a random frame from 15% to 70%, checking also how contrasted is the 
image, and dropping bad frames.

%files
%defattr(-,root,root)
%{_kde_bindir}/mplayerthumbsconfig
%{_kde_libdir}/kde4/videopreview.so
%{_kde_appsdir}/videothumbnail
%{_kde_datadir}/config.kcfg/mplayerthumbs.kcfg
%{_kde_datadir}/kde4/services/videopreview.desktop

#--------------------------------------------------------------------------

%prep
%setup -q

%build

%cmake_kde4

%make

%install
rm -rf %buildroot

%makeinstall_std -C build

%clean
rm -rf %buildroot
