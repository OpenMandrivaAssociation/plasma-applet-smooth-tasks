%define name	plasma-applet-smooth-tasks
%define version	 0
%define year	2010
%define month	02
%define day	27
%define svn	%year%month%day
%define release	%mkrel 0.%svn.2
%define Summary	 A smooth taskbar replacement


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://www.kde-look.org/CONTENT/content-files/101586-smooth-tasks-src-wip-%{year}-%{month}-%{day}.tar.bz2
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		https://www.kde-look.org/content/show.php/Smooth+Tasks?content=101586
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-runtime => 4.3
Provides:	plasma-applet

%description
This taskbar replacement has window peeking similar to Windows 7 when
you use the kwin 'highlight window' effect. Even if this effect is not
used you can click the tooltip in order to activate the corresponding
window.

%files  -f plasma_applet_smooth-tasks.lang
%defattr(-,root,root)
%doc	ChangeLog COPYING  INSTALL  README
%_kde_libdir/kde4/plasma_applet_smooth-tasks.so
%_kde_services/plasma-applet-smooth-tasks.desktop

#------------------------------------------------------------------------------

%prep
%setup -q -n smooth-tasks-src-wip-%year-%month-%day

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang plasma_applet_smooth-tasks
%clean
%__rm -rf %{buildroot}
