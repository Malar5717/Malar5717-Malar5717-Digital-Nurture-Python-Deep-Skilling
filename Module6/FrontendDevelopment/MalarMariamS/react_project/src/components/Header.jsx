function Header({siteName}) {
  return (
    <>
    <h1>{siteName}</h1>
      <nav>
        <ul>
            <li><a href="">Home</a></li>
            <li><a href="">Courses</a></li>
            <li><a href="">Profile</a></li>
        </ul>
      </nav>
    </>
  )
}

export default Header

