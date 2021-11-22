#include <Python.h>

/**
* print_python_list_info - prints some basic info about Python lists
* @p: pointer to a PyObject
*
* Return: Always Void
*/
void print_python_list_info(PyObject *p)
{
	int i, size, alctd;
	PyObject *py_obj;

	i = 0;
	size = Py_SIZE(p);
	alctd = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alctd);
	while (i < size)
	{
		printf("Element %d: ", i);
		py_obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(py_obj)->tp_name);
		i++;
	}
}
