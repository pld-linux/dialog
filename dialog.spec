%define		ver	1.2
%define		sdate	20130928
Summary:	A program to build tty dialog boxes
Summary(de.UTF-8):	Ein Programm zum Erstellen von tty-Dialogfeldern
Summary(fr.UTF-8):	Programme pour construire des boîtes de dialogue en mode texte
Summary(pl.UTF-8):	Dialog tworzy okienkowy interfejs użytkownika na terminalu tekstowym
Summary(tr.UTF-8):	tty diyalog kutuları oluşturan bir program
Name:		dialog
Version:	%{ver}.%{sdate}
Release:	1
Epoch:		1
License:	LGPL v2.1
Group:		Applications/Terminal
Source0:	ftp://invisible-island.net/dialog/%{name}-%{ver}-%{sdate}.tgz
# Source0-md5:	2cf55cd9d4603ffdb4b24cd6843d740c
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	932081790cd8aa857822bd2b0eafa5bb
Patch0:		%{name}-link.patch
URL:		http://invisible-island.net/dialog/dialog.html
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dialog is a utility that allows you to build user interfaces in a TTY
(text mode only). You can call dialog from within a shell script to
ask the user questions or present with choices in a more user friendly
manner.

%description -l de.UTF-8
Dialog ist ein Dienstprogramm, das das Erstellen einer
Benutzeroberfläche in einem TTY ermöglicht (nur Textmodus). Sie können
dialog mit einem Shell-Script aufrufen, um dem Benutzer auf
benutzerfreundliche Weise Fragen zu stellen oder eine Auswahl
anzubieten. Unter %{_examplesdir}/%{name}-%{version} finden Sie einige
Beispiele.

%description -l fr.UTF-8
dialog est un utilitaire permettant de construire des interfaces
utilisateur en mode texte. On peut appeler dialog à partir d'un script
shell pour poser des questions à l'utilisateur ou lui proposer des
choix de façon conviviale. Voir %{_examplesdir}/%{name}-%{version}
pour quelques exemples.

%description -l pl.UTF-8
Dialog jest narzędziem umożliwiającym stworzenie przyjaznego
interfejsu użytkownika na terminalu pracującym w trybie tekstowym. Do
programu dołączone są przykładowe skrypty, ułatwiające rozpoczęcie
pracy.

%description -l tr.UTF-8
Dialog, metin ekran için kullanıcı arayüzleri oluşturmayı sağlayan bir
araçtır. Kullanıcıya seçenekleri göstermek veya sorular sormak için,
dialog programını bir kabuk programcığı içinden çağırabilirsiniz.
Örnekler için %{_examplesdir}/%{name}-%{version} dizinine bakınız.

%package devel
Summary:	Libraries and headers files for dialog
Summary(pl.UTF-8):	Biblioteki i pliki nagółwkowe dla dialog
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	ncurses-devel >= 5.4

%description devel
Libraries and header files for dialog.

%description devel -l pl.UTF-8
Biblioteki i pliki nagłówkowe dla dialog.

%package static
Summary:	Static dialog library
Summary(pl.UTF-8):	Statyczna biblioteka dialog
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static dialog library.

%description static -l pl.UTF-8
Statyczna biblioteka dialog.

%prep
%setup -q -n %{name}-%{ver}-%{sdate}
#%patch0 -p1

%build
%configure \
	--with-libtool \
	--with-ncursesw \
	--enable-nls \
	--enable-widec

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a samples/* dialog.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/dialog
%attr(755,root,root) %{_libdir}/libdialog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdialog.so.11
%{_mandir}/man1/dialog.1*
%lang(hu) %{_mandir}/hu/man1/dialog.1*
%lang(pl) %{_mandir}/pl/man1/dialog.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dialog-config
%attr(755,root,root) %{_libdir}/libdialog.so
%{_libdir}/libdialog.la
%{_includedir}/dialog.h
%{_includedir}/dlg_*.h
%{_mandir}/man3/dialog.3*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/README
%{_examplesdir}/%{name}-%{version}/*.txt
%{_examplesdir}/%{name}-%{version}/*.rc
%{_examplesdir}/%{name}-%{version}/dialog*
%{_examplesdir}/%{name}-%{version}/report*
%{_examplesdir}/%{name}-%{version}/setup*
%{_examplesdir}/%{name}-%{version}/testdata-8bit
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/buildlist*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/calendar*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/checklist
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/checklist9
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/checklist[!9]*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/dft*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/editbox*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/form*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/fselect*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/gauge*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/infobox*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/inputbox*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/inputmenu*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/killall
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/listing
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/menubox*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/mixedform*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/mixedgauge
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/msgbox*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/password*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/pause*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/prgbox*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/programbox*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/progress*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/radiolist*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/rangebox*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/rotated-data
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/shortlist
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/tailbox*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/textbox
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/textbox[0-9\-]*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/timebox*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/treeview*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/wheel
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/with*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/yesno*

%files static
%defattr(644,root,root,755)
%{_libdir}/libdialog.a
