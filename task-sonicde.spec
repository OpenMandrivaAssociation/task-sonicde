Summary:	Metapackage for SonicDE
Name:		task-sonicde
Version:	6.6.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/SonicDE
Requires:	%{name}-minimal = %{EVRD}
Requires:	distro-plasma-config
Requires:	bluedevil
Requires:	drkonqi
# Part of KApps, but not useful to people with computers
# that don't have optical drives -- let's not make it a
# hard requirement
Suggests:	k3b
Requires:	kbackup
Suggests:	helium-qt6
Requires:	digikam
Requires:	kamoso
Requires:	ktorrent
# Holding off until we can get rid of qt5 support in Krita entirely
#Suggests:	krita
Requires:	dolphin-plugins
Requires:	audiocd-kio
Requires:	ffmpegthumbs
Requires:	kaccounts-integration
Requires:	kaccounts-providers
Requires:	kdenetwork-filesharing
Requires:	kidentitymanagement
Requires:	kio-zeroconf
Requires:	kdeconnect
Requires:	kdegraphics-thumbnailers
Requires:	kget
# Let's not put in a hard requirement on support for a specific
# cloud provider with a non-free server side...
Suggests:	kio-gdrive
# (crazy) FIXME: need -pim task
# (tpg) kdepim
Requires:	kdepim-runtime
Requires:	akonadi-search
Requires:	akonadi-calendar-tools
Requires:	kleopatra
Requires:	kaddressbook
Requires:	kmail
Requires:	kmail-account-wizard
Requires:	kontact
Requires:	kalarm
Requires:	korganizer
Requires:	akregator
# end pim
Requires:	kdialog
# Not very useful to journald users, so only suggesting it
Suggests:	ksystemlog
Requires:	krdc
Requires:	kdenlive
Requires:	kamera
Requires:	kcalc
Requires:	kate
Requires:	kdf
Requires:	kgamma
Requires:	kwrite
Requires:	konversation
Requires:	spectacle
Requires:	krfb
Requires:	kwallet-pam
Requires:	signon-kwallet-extension
Requires:	kwave
Requires:	okular
%ifnarch %{armx}
Requires:	plymouth-kcm
%endif
Requires:	kf6-sonnet
Requires:	speech-dispatcher
Requires:	myspell-dictionary
Requires:	sddm
Requires:	sddm-kcm
Requires:	silver-sddm
Requires:  sonic-workspace-wallpapers
Requires:	skanlite
Requires:	khelpcenter
Requires:	partitionmanager
# Requires:	discover
# Requires:	discover-notifier
# Requires:	discover-backend-packagekit
Requires:	print-manager
Requires:	ssr
Requires:	(kde-gtk-config if gtk+-3.0)
#Requires:	plasma-firewall
Requires:	plasma-systemmonitor
Requires:	plasma-disks
Requires:	plasma-welcome
Suggests:	yakuake
Suggests:	skrooge
Recommends:	om-repo-picker
Recommends:	om-update-config

%description
This package is a meta-package, meaning that its purpose is to contain
the complete dependencies for running SonicDE.

%files

#----------------------------------------------------------------------------

%package minimal
Summary:	Minimal dependencies needed for SonicDE
Group:		Graphical desktop/SonicDE
# Basic
Requires:	xsettingsd
Conflicts:	xsettings-kde
Requires:	ark
Requires:	kate
Requires:	dolphin
Requires:	konsole
Requires:	nomacs
Requires:	pinentry-qt6
Requires:	libproxy-kde
Requires:	libproxy-networkmanager
Requires:  silver-theme
Requires:	breeze
Requires:	breeze-icons
Requires:	oxygen-sounds
Requires:	kf6-frameworkintegration
Requires:	kde-cli-tools
Requires:	kf6-kded
Requires:	kf6-kdeclarative
Requires:	milou
Requires:	kf6-baloo
Requires:	plasma-pa
Requires:	plasma-integration
Requires:	sonic-desktop-interface >= %{version}
Requires:	plasma-vault
Requires:	plasma-browser-integration
Requires:	sonic-workspace >= %{version}
Requires:	kdeplasma-addons
Requires:	sonic-system-info >= %{version}
# Requires:	kio-extras
Requires:	kmenuedit
Requires:	sonic-screen
Requires:	sonic-screenlocker
Requires:	kf6-kservice
Requires:	ksshaskpass
Requires:	kwalletmanager
Requires:	kwrited
Requires:	phonon4qt6-backend
Recommends:	phonon4qt6-backend-mpv
Requires:	plasma-nm
Requires:	powerdevil >= 5.8.4
Requires:	systemsettings
Requires:	kf6-solid
Requires:	polkit-kde-agent-1
Requires:	xdg-desktop-portal-kde
Requires:	distro-release-desktop
Suggests:	task-pulseaudio

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal SonicDE.

%files minimal

#----------------------------------------------------------------------------

# fork in progress

# %package mobile-minimal
# Summary:	Minimal set of packages for SonicDE Mobile
# Group:		Graphical desktop/SonicDE
# # Basic
# Requires:	pinentry-qt6
# Requires:	libproxy-kde
# Requires:	libproxy-networkmanager
# Requires:	breeze
# Requires:	breeze-icons
# Requires:	oxygen-sounds
# Requires:	kf6-frameworkintegration
# Requires:	kde-cli-tools
# Requires:	kf6-kded
# Requires:	kf6-kdeclarative
# Requires:	plasma-pa
# Requires:	plasma-integration
# Requires:	sonic-desktop-interface >= %{version}
# Requires:	plasma-vault
# Requires:	plasma-browser-integration
# Requires:	sonic-workspace >= %{version}
# Requires:  sonic-lockscreen
# Requires:	kf6-kservice
# Requires:	ksshaskpass
# Requires:	kwalletmanager
# Requires:	phonon4qt6-backend
# Requires:	qmlkonsole
# Requires:	plasma-nm
# Requires:	powerdevil >= 6.0.0
# Requires:	kf6-solid
# Requires:	polkit-kde-agent-1
# Requires:	xdg-desktop-portal-kde
# Requires:	milou
# Requires:	kconfig

# # Key SonicDE Mobile specific bits (stuff that is either
# # required or active in the default config)
# Requires:	sonic-mobile-interface
# Requires:	%mklibname Qt6VirtualKeyboard
# Requires:	kweather
# Requires:	kclock
# Requires:	angelfish
# Requires:	distro-release-desktop
# Suggests:	task-pulseaudio

# %description mobile-minimal
# This package is a meta-package, meaning that its purpose is to contain
# a minimal version of the mobile version of the Plama 5 desktop environment.


# %files mobile-minimal
# #----------------------------------------------------------------------------

# %package mobile
# Summary:	Packages for SonicDE Mobile
# Group:		Graphical desktop/KDE
# # Basic
# Requires:	%{name}-mobile-minimal = %{EVRD}
# Requires:	alligator
# Requires:	spacebar
# Requires:	maui-pix
# ###Requires:	kaidan
# Requires:	calindori
# Requires:	keysmith
# Requires:	kalk
# Requires:	plasma-phonebook
# Requires:	plasma-camera
# Requires:	index-fm
# # Requires:	telegram-desktop
# Requires:	qmlkonsole
# Requires:	buho
# Requires:	okular-mobile
# Requires:	okular-pdf
# Requires:	okular-postscript
# Requires:	okular-epub
# Requires:	okular-kimgio
# # Requires:	discover
# # Requires:	discover-backend-packagekit
# Requires:	kscreen
# Requires:	kmix
# Requires:	plasma-pa
# Requires:	vvave
# Requires:	koko
# Requires:	nota
# Requires:	station
# Requires:	communicator
# Requires:	itinerary
# Requires:	clip

# %description mobile
# This package is a meta-package, meaning that its purpose is to contain
# the mobile version of the Plasma desktop environment.

# %files mobile
#----------------------------------------------------------------------------

%prep

%build

%install
