import courses from './data.js';

const formattedCourses = courses.map((item, idx) => `${item.code} - ${item.name} (${item.credits})`);
console.log("Formatted Courses:");
console.log(formattedCourses)

const creditGreaterThan_4 = courses.filter((item) => item.credits >= 4);
console.log("Credits greater than 4:", creditGreaterThan_4.length);

const totalCredits = courses.reduce((tot, item) => tot + item.credits, 0);
console.log("Total Credits:", totalCredits);

const courseGrid = document.querySelector('.course-grid');
function displayCourseGrid(coursesList) {
    coursesList.forEach((item) => {
        const articleTag = document.createElement('article');
        articleTag.className = 'course-card';
        articleTag.innerHTML = `${item.code} - ${item.name} (${item.credits})`;
        courseGrid.appendChild(articleTag);
    });
}
displayCourseGrid(courses);

const totCreds = document.createElement('p');
totCreds.id = 'total-credits';
totCreds.textContent = `Total Credits: ${totalCredits}`;
document.body.appendChild(totCreds);

const searchInput = document.getElementById('search-courses');
searchInput.addEventListener('input', (e) => {
    const filteredCourses = courses.filter((item) => item.name.toLowerCase().startsWith(e.target.value.toLowerCase()));
    console.log("filtered courses", courses)
    courseGrid.innerHTML = "";
    displayCourseGrid(filteredCourses);
});

const sortButton = document.getElementById('sort-courses');
sortButton.addEventListener('click', () => {
    const filteredCourses = courses.sort((a, b) => b.credits - a.credits);
    courseGrid.innerHTML = "";
    displayCourseGrid(filteredCourses);
});

courseGrid.addEventListener('click', (e)=>{
    const card = e.target.closest('.course-card');
    if (!card) return;
    alert(card.textContent);
});
