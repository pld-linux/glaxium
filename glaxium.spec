Summary:	OpenGL-based space-ship "shoot-em-up"
Summary(pl.UTF-8):	Trójwymiarowa kosmiczna strzelanka
Name:		glaxium
Version:	0.5
Release:	5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://xhosxe.free.fr/glaxium/%{name}_%{version}.tar.gz
# Source0-md5:	ea6d6f8b4ebb7c73b74af64d83f45cb7
Patch0:		%{name}-gcc4.patch
Patch1:		%{name}-startup_crash.patch
URL:		http://xhosxe.free.fr/glaxium
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glaxium is an OpenGL-based space-ship "shoot-em-up" styled game. It is
designed to provide the same feel as the old 2D games of that type,
but with 3D for the special effects.

%description -l pl.UTF-8
Glaxium jest trójwymiarową grą kosmiczną wykorzystującą OpenGL. Idea
tej gry jest zaczerpnięta ze starych dwuwymiarowych strzelanek
kosmicznych.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
%patch1 -p1
sed 's/^GLAXIUM_INSTALLDIR=/GLAXIUM_INSTALLDIR=$(DESTDIR)/' Makefile.in > Makefile.in.tmp
sed 's/^GLAXIUM_HOME=/GLAXIUM_HOME=$(DESTDIR)/' Makefile.in.tmp > Makefile.in
sed 's/^MAN_DIR=/MAN_DIR=$(DESTDIR)/' Makefile.in > Makefile.in.tmp
cat Makefile.in.tmp > Makefile.in
rm -f Makefile.in.tmp

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt CHANGES.txt
%attr(755,root,root) %{_bindir}/glaxium
%{_datadir}/games/%{name}
%{_mandir}/man6/glaxium.6*
