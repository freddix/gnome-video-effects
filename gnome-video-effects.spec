Summary:	Collection of GStreamer video effects
Name:		gnome-video-effects
Version:	0.4.1
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-video-effects/0.4/%{name}-%{version}.tar.xz
# Source0-md5:	aa0838f5be12f524ba5622e1b61d21b1
URL:		http://live.gnome.org/GnomeVideoEffects
BuildRequires:	gettext-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of GStreamer effects to be used in different GNOME
Modules.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gnome-video-effects
%{_npkgconfigdir}/gnome-video-effects.pc

