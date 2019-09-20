# Image mattiong	
## Performance:


![flowers-compA](./test_images/small/flowers-compA.jpg)
![backgroud](./test_images/small/window.jpg)
![comp](./src/comp.jpg)
### Usage:
```
python viscomp.py --matting \
                --backA ../test_images/small/flowers-backA.jpg \
                --backB ../test_images/small/flowers-backB.jpg \
                --compA ../test_images/small/flowers-compA.jpg \
                --compB ../test_images/small/flowers-compB.jpg \
                --alphaOut alpha.tif \
                --colOut col.tif
```

               

### Input
![flowers-backA](./test_images/tiny/flowers-backA.jpg)
+
![flowers-backB](./test_images/tiny/flowers-backB.jpg)
+
![flowers-compA](./test_images/tiny/flowers-compA.jpg)
+
![flowers-compB](./test_images/tiny/flowers-compB.jpg)

### Output
![alpha](./src/alpha.jpg)
![col](./src/col.jpg)


# Image compositing 
### Usage:
```
python viscomp.py --compositing \
	            --alphaIn alpha.tif \
	            --colIn col.tif \
	            --backIn ../test_images/small/window.jpg \
	            --compOut comp.jpg
```
### Input

![alpha](./src/alpha.jpg)
+
![col](./src/col.jpg)
+
![backgroud](./test_images/tiny/window.jpg)

### Outout

![comp](./src/comp.jpg)
