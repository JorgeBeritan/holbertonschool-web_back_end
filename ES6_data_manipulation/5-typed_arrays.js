export default function createInt8TypeArray(length, position, value) {
  if (position < 0 || position > length) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const int8 = new DataView(buffer);
  int8.setInt8(position, value);
  return int8;
}
