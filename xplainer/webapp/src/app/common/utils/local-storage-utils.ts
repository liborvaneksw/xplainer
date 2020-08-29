/**
 * Returns the current JSON value associated with the given in localStorage
 * or the defaultValue if the key does not exists.
 */
export function getLocalStorageJson(key: string, defaultValue: any): any {
  const value = localStorage.getItem(key);
  if (!value) {
    return defaultValue;
  }

  const jsonValue = JSON.parse(value);
  if (!jsonValue) {
    return defaultValue;
  }

  return jsonValue;
}

/**
 * Returns the current string value associated with the given in localStorage
 * or the defaultValue if the key does not exists.
 */
export function getLocalStorageString(key: string, defaultValue: string): string {
  const value = localStorage.getItem(key);
  if (!value) {
    return defaultValue;
  }

  return value;
}

/**
 * Returns the current integer value associated with the given in localStorage
 * or the defaultValue if the key does not exists.
 */
export function getLocalStorageInteger(key: string, defaultValue: number): number {
  const value = localStorage.getItem(key);
  if (!value) {
    return defaultValue;
  }

  const intValue = parseInt(value);
  if (Number.isNaN(intValue)) {
    return defaultValue;
  }

  return intValue;
}

/**
 * Returns the current float value associated with the given in localStorage
 * or the defaultValue if the key does not exists.
 */
export function getLocalStorageFloat(key: string, defaultValue: number): number {
  const value = localStorage.getItem(key);
  if (!value) {
    return defaultValue;
  }

  const floatValue = parseFloat(value);
  if (Number.isNaN(floatValue)) {
    return defaultValue;
  }

  return floatValue;
}

/**
 * Returns the current float value associated with the given in localStorage
 * or the defaultValue if the key does not exists.
 */
export function getLocalStorageBoolean(key: string, defaultValue: boolean): boolean {
  const value = localStorage.getItem(key);
  if (!value) {
    return defaultValue;
  }
  return value && value.toLocaleLowerCase() === "true";
}
