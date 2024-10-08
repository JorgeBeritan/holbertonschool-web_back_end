const fs = require('fs');

function countStudents(path){
    try{
        const data = fs.readFileSync(path, 'utf8');
        const lines = data.split('\n').filter(line =>line.trim() !== '');
        const students = lines.slice(1);

        console.log(`Number of students: ${students.length}`);

        const fields = {};

        students.forEach(student => {
            const studentData = student.split(',');
            const firstName = studentData[0];
            const field = studentData[3];

            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstName);
        });

        for (const field in fields) {
            const list = fields[field].join(', ');
            console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
        }
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}


module.exports = countStudents;