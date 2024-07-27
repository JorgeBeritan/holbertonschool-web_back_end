export default function hasValueFromArray(set, array) {
  return array.every((i) => set.has(i));
}
