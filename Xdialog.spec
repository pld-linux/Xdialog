Name:		Xdialog
Summary:	Xdialog in replacement for the cdialog program.
Version:	1.4.1
Release:	2
Source0:	Xdialog-%{version}.tar.bz2
Group:		X11/Administration
URL:		http://xdialog.free.fr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
License:	GPL

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xdialog is designed to be a drop in replacement for the cdialog program. It
converts any terminal based program into a program with an X-windows
interface. The dialogs are easier to see and use and Xdialog adds even more
functionalities (help button+box, treeview, editbox, file selector, range
box, and much more).

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure 
make 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9fn README NEWS AUTHORS BUGS ChangeLog samples/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,NEWS,AUTHORS,BUGS,ChangeLog}.gz samples/*.gz
%attr(755,root,root) %{_bindir}/*
