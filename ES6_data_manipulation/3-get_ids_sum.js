export default function getStudentIdsSum(students) {
  return students.reduce((student) => student.id);
}
