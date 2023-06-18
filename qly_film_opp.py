class Movie():
    def __init__(self, name, director, year):
        self.name       = name
        self.director   = director
        self.year       = year
    def display_info(self):
        print("Tên phim:\t\t", self.name)
        print("Tên đạo diễn:\t", self.director)
        print("Năm xuất bản:\t", self.year)

class Movie_list:
    def __init__(self):
        self.movies = []    
    def add_movie(self, movie):
        self.movies.append(movie)
    def remove_movie(self, name):
        for movie in self.movies:
            if movie.name == name:
                self.movies.remove(movie)
                print("removed completely")
                return
            print("not found the film, u wanna remove")
    def display_movies(self):
        if self.movies:
            for idx, movie in enumerate(self.movies, start=1):
                print("THÔNG TIN BỘ PHIM", idx)
                movie.display_info()
        else:
            print("Danh sách phim trống!")       




# Định nghĩa menu hiển thị gợi ý người dùng
user_menu = '''Nhập
a - Thêm một bộ phim mới
l - Hiển thị danh sách phim
s - Tìm kiếm các bộ phim theo tên
x - Xóa phim theo tên
q - Thoát'''

movie_list = Movie_list()

user_choice = input(user_menu)

while user_choice != 'q':
    if user_choice == 'a':
        name = input("Nhập vào tên bộ phim: ")
        director = input("Nhập vào tên đạo diễn: ")
        release_year = input("Nhập vào năm phát hành: ")

        movie = Movie(name, director, release_year)
        movie_list.add_movie(movie)

    elif user_choice == 'l':
        movie_list.display_movies()

    elif user_choice == 's':
        name = input("Nhập vào tên bộ phim: ")
        movie_list.search_movie(name)

    elif user_choice == 'x':
        name = input("Nhập vào tên bộ phim: ")
        movie_list.remove_movie(name)

    user_choice = input(user_menu)
