from pathlib import Path

# path = Path(".").absolute()
# print(path)
# print(path.absolute())

# path = Path(r"E:\python_trainings\new_batch_2_2024")
# print(path)

# print(path)
# new_path = path.parent.parent
#
# print(new_path)
#
# new_path = new_path.joinpath("new_batch_2_2024", "ch9")
# print(new_path)
# print(new_path.exists())
# another_path = new_path.joinpath("abc")
# print(another_path)
# #
# # print(another_path.exists())
# if not another_path.exists():
#     another_path.mkdir()
#
# my_tmp_file = another_path.joinpath("abc.txt")
# if not my_tmp_file.exists():
#     my_tmp_file.touch()
#
# print(my_tmp_file)
# print(my_tmp_file.name)
# print(my_tmp_file.stem)
# print(type(my_tmp_file))
# print(my_tmp_file.as_posix())
# print(type(my_tmp_file.as_posix()))
#
# print(my_tmp_file.is_dir())
# print(my_tmp_file.is_file())
#
# print(Path.cwd())
# # print(my_tmp_file.unlink())
#
# # my_tmp_file.parent.rmdir()

path = Path(".").absolute().parent
print(path)

# print(list(path.iterdir()))
# print(list(path.glob("ch*")))
# print(list(path.glob("*.py")))
# path = path.joinpath("ch9")

# print(list(path.rglob("*")))

# dir_lst = [p for p in path.rglob("*") if p.is_dir()]
# print(dir_lst)
#
# dir_lst = [p.name for p in path.rglob("*.py")]
# print(dir_lst)
