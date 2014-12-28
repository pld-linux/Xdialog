Summary:	Xdialog - replacement for the dialog program
Summary(pl.UTF-8):	Xdialog - zamiennik dla programu cdialog
Name:		Xdialog
Version:	2.3.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://xdialog.free.fr/%{name}-%{version}.tar.bz2
# Source0-md5:	0671f8353717513bf1f0ebc80e9710f6
Patch0:		%{name}-configure.patch
URL:		http://xdialog.dyns.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 1:2.2.0
BuildRequires:	pkgconfig
Provides:	xdialog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xdialog is designed to be a drop in replacement for the cdialog
program. It converts any terminal based program into a program with an
X Window interface. The dialogs are easier to see and use and Xdialog
adds even more functionalities (help button+box, treeview, editbox,
file selector, range box, and much more).

%description -l pl.UTF-8
Xdialog jest zaprojektowany by być odpowiednikiem, zamiennikiem dla
programu cdialog. Dzięki niemu dowolny terminalowy program używający
dialogu można zamienić w program z interfejsem X Window.

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

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no_NO,nb}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sv{_SE,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README doc/*.{html,png} samples/
%attr(755,root,root) %{_bindir}/Xdialog
%{_mandir}/man1/Xdialog.1*
