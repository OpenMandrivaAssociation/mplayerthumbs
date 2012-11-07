Name:		mplayerthumbs
Version: 4.9.3
Release: 1
Epoch:		3
Summary:	Video thumbnail generator for KDE4 file managers
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/mplayerthumbs
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
Requires:	kdebase4-runtime

%description
MPlayerThumbs is a video thumbnail generator for KDE file managers
(Konqueror, Dolphin, ...), now available also for KDE 4.
It needs mplayer (of course) to generate thumbnails, and it contains
no linking to any library, so in a x86_64 system you can freely use the
32bit mplayer binary with win32codecs by configuring the application
launching the mplayerthumbsconfig helper application.
It catches a random frame from 15% to 70%, checking also how contrasted
is the image, and dropping bad frames.

%files
%{_kde_bindir}/mplayerthumbsconfig
%{_kde_libdir}/kde4/videopreview.so
%{_kde_appsdir}/videothumbnail
%{_kde_datadir}/config.kcfg/mplayerthumbs.kcfg
%{_kde_services}/videopreview.desktop

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

