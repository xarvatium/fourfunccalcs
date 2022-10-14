;; Defined here so the while loop knows what it is
(def operator "")

;; Defining a print function to print then flush
;; Not defined as `printf` because that already exists
(defn fprint [str]
  (print str)
  (flush)
)

;; Defining a function to convert a string to integer
;; Called atoi to mimic the C function
(defn atoi [str]
  (let [n (read-string str)]
    (if (number? n) n nil)))

(while (not= operator "z")
  (fprint "Operator (+, -, *, /, `z` to exit): ")
  (def operator (read-line))
  (if (not= operator "z")
    (do
      (fprint "First: ")
      (def num1 (read-line))

      (fprint "Second: ")
      (def num2 (read-line))

      (cond
        (= operator "+") (println (+ (atoi num1) (atoi num2)))
        (= operator "-") (println (- (atoi num1) (atoi num2)))
        (= operator "*") (println (* (atoi num1) (atoi num2)))
        (= operator "/") (println (/ (atoi num1) (atoi num2)))
        :else (println "Invalid input detected, please try again.")
        )
      )
    (println "Exiting...")
    )
)
