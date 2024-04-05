Q=[280,120;12,8]
q=[575;20]
A=Q*inv(diag(q))
[prop, lambdas]=spec(A')
[lambdad, ind]=max(real(lambdas))
p=prop(1:2,ind(1))/prop(1,ind(1))
r=(1-lambdad)/lambdad