export default function concatArrays(array1, array2, string) {
  let concat = [...array1, ...array2, ...string];
  return concat
}
