Summary:	Xdialog - replacement for the dialog program
Summary(pl):	Xdialog - zamiennik dla programu cdialog
Name:		Xdialog
Version:	2.1.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://thgodef.nerim.net/xdialog/%{name}-%{version}.tar.bz2
# Source0-md5:	fb8177e9d87504329cf08b07d91586a0
Patch0:		%{name}-configure.patch
URL:		http://xdialog.dyns.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xdialog is designed to be a drop in replacement for the cdialog
program. It converts any terminal based program into a program with an
X Window interface. The dialogs are easier to see and use and Xdialog
adds even more functionalities (help button+box, treeview, editbox,
file selector, range box, and much more).

%description -l pl
Xdialog jest zaprojektowany by byæ odpowiednikiem, zamiennikiem dla
programu cdialog. Dziêki niemu dowolny terminalowy program u¿ywaj±cy
dialogu mo¿na zamieniæ w program z interejsem X Window.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	doc_DATA=

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS AUTHORS BUGS ChangeLog samples/
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
