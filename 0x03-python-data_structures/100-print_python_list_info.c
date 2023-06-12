#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints information about a PyObject struct
 * @p: pointer to a PyObject struct.
 *
*/
void print_python_list_info(PyObject *p)
{
	PyListObject *p_obj = (PyListObject *)p;
	int i, allocated, num_items;

	allocated = p_obj->allocated;
	num_items = p_obj->ob_base.ob_size;

	printf("[*] Size of the Python List = %d", num_items);
	printf("[*] Allocated = %d", allocated);

	for (i = 0; i < num_items; i++)
	{
		printf("Element %s: ", p_obj->ob_base.ob_base.ob_type->tp_name);
	}
}
