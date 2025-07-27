from .string import snake_case, make_method_name, pascal_case
from unittest import TestCase


class TestSnakeCase(TestCase):
    def test_simple(self):
        self.assertEqual(snake_case("HelloWorld"), "hello_world")

    def test_with_spaces(self):
        self.assertEqual(snake_case("Hello World"), "hello_world")

    def test_with_hyphens(self):
        self.assertEqual(snake_case("Hello-World"), "hello_world")

    def test_leading_trailing_spaces(self):
        self.assertEqual(snake_case("  HelloWorld  "), "hello_world")

    def test_empty_string(self):
        self.assertEqual(snake_case(""), "")

    def test_slashes(self):
        self.assertEqual(snake_case("Hello/World"), "hello_world")

    def test_dots(self):
        self.assertEqual(snake_case("Hello.World"), "hello_world")

    def test_sequential_uppercase(self):
        self.assertEqual(snake_case("HTTPResponse"), "http_response")


class TestPascalCase(TestCase):
    def test_simple(self):
        self.assertEqual(pascal_case("hello_world"), "HelloWorld")

    def test_with_spaces(self):
        self.assertEqual(pascal_case("hello world"), "HelloWorld")

    def test_with_hyphens(self):
        self.assertEqual(pascal_case("hello-world"), "HelloWorld")

    def test_leading_trailing_spaces(self):
        self.assertEqual(pascal_case("  hello world  "), "HelloWorld")

    def test_empty_string(self):
        self.assertEqual(pascal_case(""), "")

    def test_slashes(self):
        self.assertEqual(pascal_case("hello/world"), "HelloWorld")

    def test_dots(self):
        self.assertEqual(pascal_case("hello.world"), "HelloWorld")


class TestMakeMethodName(TestCase):
    def test_simple(self):
        self.assertEqual(make_method_name("get", "/hello/world"), "get_hello_world")

    def test_with_path_params(self):
        self.assertEqual(
            make_method_name("post", "/hello/{name}/world"), "post_hello_by_name_world"
        )

    def test_with_multiple_path_params(self):
        self.assertEqual(
            make_method_name("put", "/api/v1/resource/{id}/attributes/{attr}"),
            "put_api_v1_resource_by_id_attributes_by_attr",
        )

    def test(self):
        self.assertEqual(
            make_method_name("get", "/contas/{agencia}-{conta}/situacao"),
            "get_contas_by_agencia_by_conta_situacao",
        )
