import './App.css'
import Header from './components/Header'
import Footer from './components/Footer'
import CourseCard from './components/CourseCard'
// import { useState } from 'react'

function App() {

  // const [courses, setCourses] = useState([]);

  return (
    <>
      <Header siteName={'Student Portal'}/>
      <CourseCard name='Tamil' code='T001' credits={4} grade='II'/>
      <Footer />
    </>
  )
}

export default App
