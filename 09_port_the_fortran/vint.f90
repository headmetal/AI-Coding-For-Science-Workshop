!-----------------------------------------------------------------------
! vint: vertical integral of a tracer over the water column
!
!   tracer(i,j,k)   tracer concentration at cell centres
!   dz(k)           nominal thickness of level k (m)
!   kmt(i,j)        number of wet levels in column (i,j); 0 = land
!   frac(i,j)       fraction of the bottom wet cell that is open (0 < frac <= 1)
!   vint(i,j)       output: integral of tracer * thickness (tracer units * m)
!
! Arrays are column-major (i fastest). Levels are numbered 1 (surface) to nk.
!-----------------------------------------------------------------------
subroutine vint(tracer, dz, kmt, frac, ni, nj, nk, result)
  implicit none
  integer, intent(in) :: ni, nj, nk
  real(8), intent(in) :: tracer(ni, nj, nk)
  real(8), intent(in) :: dz(nk)
  integer, intent(in) :: kmt(ni, nj)
  real(8), intent(in) :: frac(ni, nj)
  real(8), intent(out) :: result(ni, nj)

  integer :: i, j, k, kb

  do j = 1, nj
    do i = 1, ni
      result(i, j) = 0.0d0
      kb = kmt(i, j)
      if (kb .eq. 0) cycle                      ! land column
      ! full cells above the bottom cell
      do k = 1, kb - 1
        result(i, j) = result(i, j) + tracer(i, j, k) * dz(k)
      end do
      ! partial bottom cell
      result(i, j) = result(i, j) + tracer(i, j, kb) * dz(kb) * frac(i, j)
    end do
  end do

end subroutine vint
