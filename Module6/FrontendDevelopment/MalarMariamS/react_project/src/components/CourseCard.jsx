function CourseCard({name, code, credits, grade}) {
  return (
    <div className='course-card'>
        <h3>{code} - {name}</h3>
        <p>credits: {credits}</p>
        <p>grade: {grade}</p>
    </div>
  )
}

export default CourseCard
