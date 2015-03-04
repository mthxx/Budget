# Maintainer: Marc Thomas mat@mthx.org
pkgname=budget
pkgver=0.0.1
pkgrel=1
pkgdesc="Personal finance application built for the Gnome desktop (alpha version)"
arch=(i686 x86_64)
url="http://mthx.org/projects/budget/"
license=('GPL')
groups=()
depends=()
makedepends=()
optdepends=()
provides=('budget')
conflicts=()
replaces=()
backup=()
options=()
install= budget.install
changelog=
source=(https://github.com/mthxx/Budget.git)
#source=($pkgname-$pkgver.tar.gz)
noextract=()
sha256sums=() #autofill using updpkgsums

build() {
  cd "$pkgname-$pkgver"

  ./configure --prefix=/usr
  make
}

package() {
    cd "$pkgname-$pkgver"
    make DESTDIR="$pkgdir/" install
}
