"use strict";
var KTSigninGeneral = function() {
    var t, e, r;
    return {
        init: function() {
            t = document.querySelector("#kt_sign_in_form"), 
            e = document.querySelector("#kt_sign_in_submit"), 
            r = FormValidation.formValidation(t, {
                fields: {
                    email: {
                        validators: {
                            regexp: {
                                regexp: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                                message: "The value is not a valid email address"
                            },
                            notEmpty: {
                                message: "Email address is required"
                            }
                        }
                    },
                    password: {
                        validators: {
                            notEmpty: {
                                message: "The password is required"
                            }
                        }
                    }
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger,
                    bootstrap: new FormValidation.plugins.Bootstrap5({
                        rowSelector: ".fv-row",
                        eleInvalidClass: "",
                        eleValidClass: ""
                    })
                }
            }), 

            e.addEventListener("click", (function(i) {
                i.preventDefault(), 
                r.validate().then((function(r) {
                    if ("Valid" == r) {
                        e.setAttribute("data-kt-indicator", "on"), 
                        e.disabled = !0;

                        const actionUrl = e.closest("form").getAttribute("action");
                        if (!actionUrl) {
                            console.error("Form action URL is missing or invalid.");
                            return;
                        }

                        console.log("Form action:", actionUrl);
                        console.log("Form data:", {
                            email: t.querySelector('[name="email"]').value,
                            password: t.querySelector('[name="password"]').value
                        });

                        // Send login request to the server
                        axios.post(actionUrl, {
                            email: t.querySelector('[name="email"]').value,
                            password: t.querySelector('[name="password"]').value
                        }, {
                            headers: {
                                'X-CSRFToken': '{{ csrf_token }}',
                                'Content-Type': 'application/json'
                            }
                        })
                            .then((response) => {
                                if (response.data.success) {
                                    // Login successful
                                    Swal.fire({
                                        text: response.data.message || "You have successfully logged in!",
                                        icon: "success",
                                        buttonsStyling: !1,
                                        confirmButtonText: "Ok, got it!",
                                        customClass: {
                                            confirmButton: "btn btn-primary"
                                        }
                                    }).then(() => {
                                        const redirectUrl = t.getAttribute("data-kt-redirect-url");
                                        if (redirectUrl) {
                                            location.href = redirectUrl;
                                        }
                                    });
                                } else {
                                    // Login failed
                                    Swal.fire({
                                        text: response.data.message || "Sorry, the email or password is incorrect.",
                                        icon: "error",
                                        buttonsStyling: !1,
                                        confirmButtonText: "Ok, got it!",
                                        customClass: {
                                            confirmButton: "btn btn-primary"
                                        }
                                    });
                                }
                            })
                            .catch((error) => {
                                console.error("Error details:", error);
                                console.error("Error response:", error.response);
                                Swal.fire({
                                    text: "Sorry, looks like there are some errors detected, please try again.",
                                    icon: "error",
                                    buttonsStyling: !1,
                                    confirmButtonText: "Ok, got it!",
                                    customClass: {
                                        confirmButton: "btn btn-primary"
                                    }
                                });
                            })
                            .finally(() => {
                                // Reset the button state
                                e.removeAttribute("data-kt-indicator"), 
                                e.disabled = !1;
                            });
                    } else {
                        // Form validation failed
                        Swal.fire({
                            text: "Sorry, looks like there are some errors detected, please try again.",
                            icon: "error",
                            buttonsStyling: !1,
                            confirmButtonText: "Ok, got it!",
                            customClass: {
                                confirmButton: "btn btn-primary"
                            }
                        });
                    }
                }));
            }));
        }
    }
}();

KTUtil.onDOMContentLoaded((function() {
    KTSigninGeneral.init()
}));