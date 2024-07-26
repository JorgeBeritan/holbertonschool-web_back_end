export default function getListStudentIds(arrayType) {
  if (Array.isArray(arrayType)) {
    return arrayType.map((arrayType) => arrayType.id);
  }
  return [];
}
