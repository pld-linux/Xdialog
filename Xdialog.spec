Summary:	Xdialog in replacement for the dialog program
Summary(pl):	Xdialog jest zamiennikiem dla programu cdialog
Name:		Xdialog
Version:	2.1.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://thgodef.nerim.net/xdialog/%{name}-%{version}.tar.bz2
# Source0-md5:	379cd3983a22d98d4436e8d4f16a56e1
URL:		http://xdialog.dyns.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xdialog is designed to be a drop in replacement for the cdialog
program. It converts any terminal based program into a program with an
X Window interface. The dialogs are easier to see and use and Xdialog
adds even more functionalities (help button+box, treeview, editbox,
file selector, range box, and much more).

%description -l pl
Xdialog jest zaprojektowany by by� odpowiednikiem, zamiennikiem dla
programu cdialog. Dzi�ki niemu dowolny terminalowy program u�ywaj�cy
dialogu mo�a zamieni� w program z interejsem X Window.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS BUGS ChangeLog samples/
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
