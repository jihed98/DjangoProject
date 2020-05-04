from django.shortcuts import render


def testpage(request):
    dicttest = {}
    dicttest["test1"] = 123
    dicttest["test2"] = "ciaone bukkake hentai"
    dicttest["test"] = [1, 2, 3, 5, 8, 13, 21]
    return render(request, 'test.html', dicttest)
